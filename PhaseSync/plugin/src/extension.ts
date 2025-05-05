import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    const disposable = vscode.commands.registerCommand('phasesync.runAnalysis', () => {
        vscode.window.showInformationMessage('PhaseSync Plugin Activated');
        // Integration logic can call a backend or run Python CLI from here
    });
    context.subscriptions.push(disposable);
}

export function deactivate() {}
