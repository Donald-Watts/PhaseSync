import * as vscode from 'vscode';
import { PythonShell, Options } from 'python-shell';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('phasesync.runWeightAnalysis', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('No active editor found');
            return;
        }

        const document = editor.document;
        const filePath = document.uri.fsPath;

        try {
            const options: Options = {
                mode: 'text',
                pythonPath: 'python',
                pythonOptions: ['-u'],
                scriptPath: path.join(context.extensionPath, '..', 'scripts'),
                args: [filePath]
            };

            PythonShell.run('weight_analysis.py', options, (err, messages) => {
                if (err) {
                    vscode.window.showErrorMessage(`Weight analysis failed: ${err.message}`);
                    return;
                }
                const result = JSON.parse(messages && messages[0] ? messages[0] : '{}');
                if (result.error) {
                    vscode.window.showErrorMessage(`Weight analysis failed: ${result.error}`);
                } else {
                    vscode.window.showInformationMessage('Weight analysis completed successfully');
                    // Update status bar
                    const statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
                    statusBarItem.text = '✔ PhaseSync';
                    statusBarItem.show();
                }
            });
        } catch (error) {
            vscode.window.showErrorMessage(`Failed to run weight analysis: ${error}`);
        }
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {} 