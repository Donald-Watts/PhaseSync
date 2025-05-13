import * as vscode from 'vscode';
import { PythonShell, PythonShellError } from 'python-shell';
import * as path from 'path';
import * as fs from 'fs';

interface WeightAnalysisResult {
    success: boolean;
    message: string;
    data?: unknown;
}

export function activate(context: vscode.ExtensionContext) {
    console.log('PhaseSync is now active');

    // Register configuration
    const config = vscode.workspace.getConfiguration('phasesync');
    
    // Register commands
    let disposable = vscode.commands.registerCommand('phasesync.runWeightAnalysis', async () => {
        try {
            const editor = vscode.window.activeTextEditor;
            if (!editor) {
                vscode.window.showErrorMessage('No active editor');
                return;
            }

            const document = editor.document;
            const text = document.getText();
            
            // Get the workspace folder
            const workspaceFolder = vscode.workspace.workspaceFolders?.[0];
            if (!workspaceFolder) {
                throw new Error('No workspace folder found');
            }

            // Create temporary file for analysis
            const tempFile = path.join(workspaceFolder.uri.fsPath, '.phasesync_temp.py');
            fs.writeFileSync(tempFile, text);

            // Run weight analysis
            const result = await runWeightAnalysis(tempFile, workspaceFolder.uri.fsPath);
            
            // Clean up
            fs.unlinkSync(tempFile);

            if (result.success) {
                vscode.window.showInformationMessage(result.message);
                // TODO: Display results in a custom view
            } else {
                vscode.window.showErrorMessage(result.message);
            }
        } catch (error) {
            console.error('Weight analysis error:', error);
            vscode.window.showErrorMessage(`Error during weight analysis: ${error instanceof Error ? error.message : String(error)}`);
        }
    });

    context.subscriptions.push(disposable);
}

async function runWeightAnalysis(filePath: string, workspacePath: string): Promise<WeightAnalysisResult> {
    return new Promise((resolve) => {
        const options = {
            mode: 'text' as const,
            pythonPath: 'python',
            pythonOptions: ['-u'],
            scriptPath: workspacePath,
            args: [filePath]
        };

        PythonShell.run('scripts/weight_analysis.py', options, (err: PythonShellError | undefined, results: string[] | undefined) => {
            if (err) {
                resolve({
                    success: false,
                    message: `Analysis failed: ${err.message}`
                });
                return;
            }

            if (!results || results.length === 0) {
                resolve({
                    success: false,
                    message: 'No results returned from analysis'
                });
                return;
            }

            try {
                const result = JSON.parse(results[0]);
                resolve({
                    success: true,
                    message: 'Weight analysis completed successfully',
                    data: result
                });
            } catch (error) {
                resolve({
                    success: false,
                    message: `Failed to parse analysis results: ${error instanceof Error ? error.message : String(error)}`
                });
            }
        });
    });
}

export function deactivate() {
    // Clean up any resources
    console.log('PhaseSync is now deactivated');
} 